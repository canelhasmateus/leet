from dataclasses import dataclass

from gnosis.evernote.domain import WebResource, Iterable

String = str


@dataclass
class WebInformation:
	origin: WebResource
	associated_urls: Iterable[ WebResource ]
	associated_text: String
