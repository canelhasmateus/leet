package canelhas.languaj.languaj.nouns;

import java.util.function.Consumer;

@FunctionalInterface
public interface Effect< T > extends Functional< T, Void >, Consumer< T > {

    @Override default void accept( T t ) { apply( t );}

}
