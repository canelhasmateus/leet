from typing import Iterable

from gnosis.evernote import parse_enex_file, EnexFrame, ClipType, StyleMetadata, Note
from gnosis.evernote.domain import WebResource
from gnosis.html.parser import make_extractor

all_urls = set()


def extract_urls( note: Note, style: StyleMetadata ) -> Iterable[ WebResource ]:
	source_url = note.attributes.source_url
	style_url = style.content_source

	result = [ style_url ]
	if source_url is not None:
		result.append( source_url )

	# TODO  2021-12-25 resources url
	return result


def deal_with_bookmark( note: Note, style: StyleMetadata ):
	urls = extract_urls( note, style )

	for url in urls:
		all_urls.add( url )
		extractor = make_extractor( url )
		result = extractor.extract( url )

		if result.successful():
			continue
			# bookmark_texts[ url ] = result.value()


def deal_with_note( frame: EnexFrame ):
	style = frame.metadata.style

	if style is None:
		return

	kind = style.content_type

	if kind == ClipType.BOOKMARK:
		deal_with_bookmark( frame.note, style )


if __name__ == '__main__':
	import pathlib

	path = pathlib.Path( r'C:\Users\Mateus\Downloads\exports' )
	i = 0
	for enex in path.glob( '*.enex' ):
		notes = parse_enex_file( str( enex ) )

		for note in notes:
			deal_with_note( note )

	print( set( map( lambda x: x.domain, all_urls ) ) )
