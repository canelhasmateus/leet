#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
from base64 import b64decode
from datetime import datetime
from io import BytesIO
from re import Pattern
from typing import Iterable, Optional

from lxml import etree, html
from lxml.etree import Element
from lxml.html import HtmlElement
from pypandoc import convert_text
from toolz.functoolz import compose_left

from gnosis.evernote.domain import ResourceAttributes, EnexEntry, Resource, Note, String, NoteAttributes, NoteMetadata, StyleMetadata, MimeType, ClipType, NoteBinary, EnexFrame, WebResource
from gnosis.utils import map_with

# from pypandoc.pandoc_download import download_pandoc
# download_pandoc()

content_pattern: Pattern = re.compile( r"(?<=--en-clipped-content:)(.+?)(;|$)" ,
                                       flags = re.MULTILINE)
source_pattern: Pattern = re.compile( r"(?<=--en-clipped-source-url:)(.+?)(;|$)" ,
                                      flags = re.MULTILINE)
title_pattern: Pattern = re.compile( r"(?<=--en-clipped-source-title:)(.+?)(;|$)" ,
                                     flags = re.MULTILINE)
url_pattern: Pattern = re.compile( r"(?P<protocol>(http|https))://"
                                   r"(?P<domain>[a-zA-Z0-9_\-.]+)+" +
                                   r"(?P<path>/\S*)*"
                                   , flags = re.MULTILINE)


def as_entry( iterable: Iterable[ Element ] ) -> EnexEntry:
	f = lambda x: x.tag
	return map_with( f, iterable )


def to_note_entry( entry: Element ) -> EnexEntry:
	content = { }
	resources = [ ]
	for subelement in entry:
		name = subelement.tag
		if name == "resource":
			resources.append( subelement )
		else:
			content[ name ] = subelement
	content[ "resources" ] = resources
	return content


def to_date( resource: EnexEntry, key: String ) -> Optional[ datetime ]:
	value = resource.get( key, None )
	if value is None:
		return None

	return datetime.strptime( value.text, "%Y%m%dT%H%M%SZ" )


def to_text( resource: EnexEntry, key: String ) -> Optional[ String ]:
	value = resource.get( key, None )
	if value is None:
		return None

	return value.text


def make_note_attributes( attribute_entry ):
	source_url = to_text( attribute_entry, "source-url" )
	return NoteAttributes(
			author = to_text( attribute_entry, "author" ),
			source = to_text( attribute_entry, "source" ),
			source_url = make_web_resource( source_url ),
			source_application = to_text( attribute_entry, "source-application" ),
			application_data = to_text( attribute_entry, "application-data" )
			)


def make_web_resource( url: Optional[ String ] ) -> Optional[ WebResource ]:
	if url is None:
		return None
	url = url.strip()
	match = url_pattern.search( url )
	if match is None:
		return None

	mapping = match.groupdict()
	domain = mapping[ "domain" ]
	path = mapping[ "path" ]
	return WebResource( raw = url,
	                    domain = domain,
	                    subdomain = None,
	                    path = path )


def make_resource( entry: EnexEntry ) -> Resource:
	to_attribute = compose_left( as_entry, make_resource_attributes )

	attributes = entry.get( "resource-attributes", [ ] )

	return Resource(
			data = to_text( entry, "data" ),
			mime = MimeType.of( to_text( entry, "mime" ) ),
			width = to_text( entry, "width" ),
			height = to_text( entry, "height" ),
			alternate_data = to_text( entry, "alternate-data" ),
			attributes = to_attribute( attributes )
			)


def make_note( entry: EnexEntry ) -> Note:
	to_resource = compose_left( as_entry, make_resource )
	to_note_attribute = compose_left( as_entry, make_note_attributes )
	to_content = compose_left( lambda x: to_text( x, "content" ), make_content )

	attributes = entry.get( "note-attributes", [ ] )
	resources = entry.get( "resources", [ ] )

	return Note(
			title = to_text( entry, "title" ),
			created = to_date( entry, "created" ),
			updated = to_date( entry, "updated" ),
			content = to_content( entry ),
			attributes = to_note_attribute( attributes ),
			resources = [ to_resource( resource ) for resource in resources ]
			)


def make_resource_attributes( entry: EnexEntry ) -> ResourceAttributes:
	source_url = to_text( entry, "source-url" )
	return ResourceAttributes(
			source_url = make_web_resource( source_url ),
			file_name = to_text( entry, "file-name" ),
			attachment = to_text( entry, "attachment" ),
			application_data = to_text( entry, "application-data" )
			)


def _parse_content( content ):
	text = convert_text( content, 'org', format = 'html' )
	return text


def _parse_resource( resource ):
	rsc_dict = { }
	for elem in resource:
		if elem.tag == 'data':
			# Some times elem.text is None
			rsc_dict[ elem.tag ] = b64decode( elem.text ) if elem.text else b''
			rsc_dict[ 'hash' ] = hashlib.md5( rsc_dict[ elem.tag ] ).hexdigest()
		else:
			rsc_dict[ elem.tag ] = elem.text

	return rsc_dict


def parse_enex_file( path: str ) -> Iterable[ EnexFrame ]:
	elem: Element

	context = etree.iterparse( path, encoding = 'utf-8', huge_tree = True, recover = False )
	for _, elem in context:
		if elem.tag == "note":
			content = to_note_entry( elem )
			note = make_note( content )
			yield make_frame( note )

def parse_enex_string( string: str ) -> Iterable[ EnexFrame ]:
	elem: Element

	context = etree.iterparse( BytesIO( string.encode( 'utf-8' ) ), encoding = 'utf-8', huge_tree = True, recover = False )
	for _, elem in context:
		if elem.tag == "note":
			content = to_note_entry( elem )
			note = make_note( content )
			yield make_frame( note )

def make_content( content: String ) -> HtmlElement:
	return html.fromstring( content )


def match_text( pattern: Pattern, text: String ) -> Optional[ String ]:
	match = re.search( pattern, text )
	if match is None:
		return None
	return match.group( 1 )


def make_style_metadata( html_element: HtmlElement ) -> Optional[ StyleMetadata ]:
	attributes = html_element.attrib
	style = attributes.get( "style", "" )

	content = match_text( content_pattern, style )
	url = match_text( source_pattern, style )
	title = match_text( title_pattern, style )

	if any( [ content, url, title ] ):
		return StyleMetadata(
				content_type = ClipType.of( content ),
				content_source = make_web_resource( url ),
				content_title = title
				)
	return None


def parse_content( note: Note ) -> Optional[ StyleMetadata ]:
	result = [ ]
	if note.content is not None:
		direct_children = note.content.getchildren()
		for html_element in direct_children:
			style_metadata = make_style_metadata( html_element )
			if style_metadata is not None:
				result.append( style_metadata )

	length = len( result )
	if length == 0:
		return None
	if length == 1:
		return result[ 0 ]
	raise Exception( "Multiple style metadata found" )


def parse_resource_data( note: Note ) -> Iterable[ NoteBinary ]:
	mime_dict = {

			MimeType.GIF : lambda x: x,
			MimeType.INK : lambda x: x,
			MimeType.JPEG: lambda x: x,
			MimeType.MPEG: lambda x: x,
			MimeType.PDF : lambda x: x,
			MimeType.PNG : lambda x: x,
			MimeType.WAV : lambda x: x,

			}
	result = [ ]
	for resource in note.resources:
		if resource.data is not None and resource.mime is not None:
			action = mime_dict[ resource.mime ]
			decoded = action( resource.data )

			value = NoteBinary( value = decoded, mime = resource.mime )
			result.append( value )

	return result


def make_frame( note: Note ) -> EnexFrame:
	return EnexFrame(
			note = note,
			metadata = make_metadata( note ),
			)


def make_metadata( note: Note ) -> NoteMetadata:
	style = parse_content( note )
	data = parse_resource_data( note )

	return NoteMetadata( style = style,
	                     binaries = data )
