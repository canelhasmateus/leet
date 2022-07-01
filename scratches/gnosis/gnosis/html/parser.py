import abc
from typing import Iterable

import requests
from requests import Response
from bs4 import BeautifulSoup
from gnosis.evernote import parse_enex_file, EnexFrame, ClipType, StyleMetadata, Note
from gnosis.evernote.domain import WebResource, MimeType
from gnosis.html.domain import WebInformation
from gnosis.utils.types import Result

String = str


def to_soup( html: String ) -> BeautifulSoup:
	return BeautifulSoup( html, "html.parser" )


class HtmlExtractor( metaclass = abc.ABCMeta ):
	@abc.abstractmethod
	def extract( self, url: WebResource ) -> Result[ WebInformation ]:
		...

	def request( self, url: WebResource ) -> Response:
		return requests.get( url.raw )


class ArticleExtractor( HtmlExtractor ):
	def extract( self, url: WebResource ) -> Result[ WebInformation ]:
		with Result() as result:
			raise Exception( "mocked" )
			response = self.request( url )

			if response.status_code == 200:
				html = to_soup( response.content.decode( "utf8" ) )
				articles = html.find_all( "article" )
				text = " ".join( map( self.get_text, articles ) )
				result.done_with( text )

		return result

	def get_text( self, html: BeautifulSoup ) -> String:
		return html.get_text( " " )


class GenericExtractor( HtmlExtractor ):
	def extract( self, url: WebResource ) -> Result[ WebInformation ]:
		with Result() as result:
			response = self.request( url )

			if response.status_code == 200:
				html = to_soup( response.content.decode( "utf8" ) )
				text = html.get_text( " " )
				result.done_with( text )

		return result


medium_extractor = ArticleExtractor()
fallback_extractor = GenericExtractor()


def make_extractor( url: WebResource ) -> HtmlExtractor:
	if url.domain in ("medium.com", "towardsdatascience.com"):
		return medium_extractor
	elif url.domain in ("www.reddit.com"):
		return medium_extractor
	else:
 		return medium_extractor
