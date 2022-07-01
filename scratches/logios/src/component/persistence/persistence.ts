import { graphql } from "@octokit/graphql";


export interface FileDescriptor {
	path: string
	contents: string
}

export interface GithubAuth {
	token: string
	owner: string
	repo: string
	branch: string
}

export interface CommitData {
	auth: GithubAuth
	message: string
	files: FileDescriptor[]
}

export enum PersistenceKey {
	GITHUB = "github"
}

export async function toGithub( commit: CommitData ) {

	let graphClient = graphql.defaults( {
											headers: {
												authorization: `token ${ commit.auth.token }`
											}
										} );

	//todo can we do this in only one request?
	let headRequest = await graphClient( {
											 query: `
											  query lastCommit($owner: String! , $repo: String! , $ref: String!) {
												  repository(owner: $owner, name:$repo) {
													  ref(qualifiedName: $ref) {
														  target {
															  oid
															  commitUrl
														  }
													  }
												  
												  }
											  }
											  `,
											 owner: commit.auth.owner,
											 repo:  commit.auth.repo,
											 ref:   `${ commit.auth.branch }`
										 } )

	return await graphClient( {
								  query: `mutation ($input: CreateCommitOnBranchInput!) {
		createCommitOnBranch(input: $input) { commit { url } } } `,
								  input: {
									  branch:          {
										  repositoryNameWithOwner: `${ commit.auth.owner }/${ commit.auth.repo }`,
										  branchName:              commit.auth.branch
									  },
									  expectedHeadOid: headRequest.repository.ref.target.oid,
									  fileChanges:     {
										  additions:
											  commit.files.map( file => ( {
												  path:     file.path,
												  contents: btoa( file.contents )
											  } ) )

									  },
									  message:         { headline: "Logios", body: commit.message }
								  }
							  } )


}

function parseLoadResponse( repository ) {

	let files = repository.repository.object.entries
	console.log( repository )
	return files.filter( ( fileobj ) => {
			return fileobj.type == "blob" && fileobj.object.isBinary == false
		} )
		.map( ( fileobj ) => {
			return {
				name:    fileobj.name,
				content: fileobj.object.text
			}
		} )

}

export async function listGithub( auth: GithubAuth ) {

}

export async function fromGithub( auth: GithubAuth ) {

	let graphClient = graphql.defaults( {
											headers: {
												authorization: `token ${ auth.token }`
											}
										} );

	return await graphClient( {
								  query: `query RepoFiles($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    object(expression: "HEAD:") {
      ... on Tree {
        entries {
          name
          type
          mode
          
          object {
            ... on Blob {
              byteSize
              text
              isBinary
            }
          }
        }
      }
    }
  }
} `,
								  owner: auth.owner, name: auth.repo
							  } ).then( parseLoadResponse )


}

export function writeKey( key: PersistenceKey, value: string ) {
	window.localStorage.setItem( key, value );
}

export function loadKey( key: PersistenceKey ): string {
	return window.localStorage.getItem( key );
}

export function writeObject( key: PersistenceKey, value: object ) {


	let json = JSON.stringify( value || {} );

	window.localStorage.setItem( key, json );

}

export function loadObject( key: PersistenceKey ): object {

	let json  = window.localStorage.getItem( key );
	var parse = JSON.parse( json );
	return parse || {};
}

export function getGithubAuth(): GithubAuth {
	return loadObject( PersistenceKey.GITHUB ) as GithubAuth
}