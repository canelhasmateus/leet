package canelhas.languaj.languaj.verbs;

import canelhas.languaj.languaj.nouns.Functional;

import java.util.regex.Pattern;

public class StringVerbs {
    public static Functional< String, String > findWith( Pattern pattern ) {
        return s -> {
            final var matcher = pattern.matcher( s );
            matcher.find();
            return matcher.group();
        };

    }
}
