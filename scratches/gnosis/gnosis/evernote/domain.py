from __future__ import annotations
import enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Mapping, List, Any
from lxml.etree import Element
from lxml.html import HtmlElement

List = List
String = str
EnexEntry = Mapping[ String, Element ]
Base64 = String


class MimeType( enum.Enum ):
	HTML = "text/html"
	GIF = "image/gif"
	INK = "application/vnd.evernote.ink"
	JPEG = "image/jpeg"
	MPEG = "audio/mpeg"
	PDF = "application/pdf"
	PNG = "image/png"
	WAV = "audio/wav"

	@classmethod
	def of( cls, value: String ) -> Optional[ MimeType ]:
		for m in MimeType:
			if m.value == value:
				return m
		return None


class ClipType( enum.Enum ):
	BOOKMARK = "bookmark"
	ARTICLE = "article"
	SIMPLIFIED = 'simplified'
	SELECTION = "selection"
	SCREENSHOT = "screenshot"
	TOPSITE = "topsite"
	PDF = "pdf"
	FULL_PAGE = "fullPage"

	@classmethod
	def of( cls, value: String ) -> Optional[ ClipType ]:
		for m in ClipType:
			if m.value == value:
				return m
		return None


@dataclass( frozen = True )
class NoteAttributes:
	author: Optional[ String ]
	source: Optional[ String ]
	source_url: Optional[ WebResource ]
	source_application: Optional[ String ]
	application_data: Optional[ String ] = field( repr = False )


@dataclass( frozen = True )
class Note:
	resources: List[ Resource ]
	title: String
	created: Optional[ datetime ]
	updated: Optional[ datetime ]
	content: HtmlElement = field( repr = False )
	attributes: NoteAttributes


@dataclass( frozen = True )
class ResourceAttributes:
	source_url: Optional[ WebResource ]
	file_name: Optional[ String ]
	attachment: Optional[ String ]
	application_data: Optional[ String ] = field( repr = False )


@dataclass( frozen = True )
class Resource:
	data: Optional[ Base64 ] = field( repr = False )
	mime: Optional[ MimeType ]
	width: Optional[ String ]
	height: Optional[ String ]
	alternate_data: Optional[ String ] = field( repr = False )
	attributes: ResourceAttributes


@dataclass( frozen = True )
class NoteMetadata:
	style: Optional[ StyleMetadata ]
	binaries: List[ NoteBinary ]


@dataclass( frozen = True )
class NoteBinary:
	value: Any = field( repr = False )
	mime: MimeType


@dataclass( frozen = True )
class StyleMetadata:
	content_type: Optional[ ClipType ]
	content_source: Optional[ WebResource ]
	content_title: Optional[ String ]


@dataclass( frozen = True )
class EnexFrame:
	note: Note
	metadata: NoteMetadata

@dataclass( frozen = True)
class WebResource:
	raw: String
	domain: String
	subdomain: Optional[ String ]
	path: Optional[ String ]
	...

