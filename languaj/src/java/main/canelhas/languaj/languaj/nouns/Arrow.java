package canelhas.languaj.languaj.nouns;

import java.util.function.UnaryOperator;

@FunctionalInterface
public interface Arrow< K > extends Functional< K, K >, UnaryOperator< K > {
}
