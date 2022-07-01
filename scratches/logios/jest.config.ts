export default {

	moduleFileExtensions:       [ 'svelte', "ts", "js" ],
	setupFiles:                 [
		"jest-canvas-mock"
	],
	testEnvironment:            'jsdom',
	testMatch:                  [ '<rootDir>/**/*.jest.ts', "<rootDir>/**/*.spec.*" ],
	testPathIgnorePatterns:     [ '/node_modules/' ],
	coverageDirectory:          './coverage',
	coveragePathIgnorePatterns: [ 'node_modules', 'src/database', 'src/test', 'src/types' ],
	reporters:                  [ 'default' ],
	globals:                    { 'ts-jest': { diagnostics: false } },
	transform:                  {
		"^.+\\.svelte$": [ "svelte-jester", { "preprocess": true } ],
		"^.+\\.ts$":     "ts-jest",
	},
};