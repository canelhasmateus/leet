from __future__ import annotations
import enum
from typing import Mapping
import sys
from boto3.session import Session

import os

String = str
Environment = Mapping[ String, String ]


class EnvironStatus( enum.Enum ):
	BOTH = enum.auto()
	NONE = enum.auto()
	ONE = enum.auto()

	@classmethod
	def of( cls, environ: Environment ) -> EnvironStatus:
		key = environ.get( 'AWS_KEY', None )
		secret = environ.get( 'AWS_SECRET', None )
		if key and secret:
			return EnvironStatus.BOTH
		elif key or secret:
			return EnvironStatus.ONE
		else:
			return EnvironStatus.NONE


status = EnvironStatus.of( os.environ )


def create_session() -> Session:
	if status == EnvironStatus.NONE:
		print( 'No AWS environment variables set. Using the default machine profile.' )
		return Session( profile_name = "default" )
	elif status == EnvironStatus.BOTH:
		print( 'Using environment variables' )
		return Session( aws_access_key_id = os.environ[ 'AWS_KEY' ],
		                aws_secret_access_key = os.environ[ 'AWS_SECRET' ] )
	else:
		print( 'Only one of the AWS environment variables are set. Be sure to use both.' )
		sys.exit()


aws_session = create_session()
