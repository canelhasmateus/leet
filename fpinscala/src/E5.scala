object E5 {


  object ex1 {
    val desc =
      """EXERCISE 1: Write a function to convert a `Stream` to a `List`, which will
      force its evaluation and let us look at it in the REPL. You can convert to the
    regular type in the standard library. You can place this and other functions
      that accept a `Stream` inside the `Stream` trait"""

    def myToList[A](stream: LazyList[A]): List[A] = {
      return stream.toList
    }

    def main(args: Array[String]): Unit = {
      println("Exercise 1: ")
      print(ex1.myToList(LazyList(1, 2, 3, 4, 5)) == List(1, 2, 3, 4, 4))
    }

  }

  object ex2 {
    val desc = """Write a function `take` for returning the first n elements of a `Stream` """

    def take[A](n: Integer): Stream[A] = {
???
    }

  }

  object ex3 {
    val desc = """Write the function `takeWhile` for returning all starting elements of a `Stream` that match the given predicate """
  }

  object ex4 {
    val desc =
      """Implement `forAll` which checks that all elements in the `Stream` match a given predicate. Your implementation should terminate the traversal as soon as it ecounter a non-matching value."""
  }

  object ex5 {
    val desc =
      """
        r|Use `foldRight` to implement `takeWhile`.
        |This will construct a stream incrementally, and only if the values in the result are demanded by some other expression.
        |""".stripMargin
  }

  object ex6 {
    val desc =
      """
        r|Implement `map`, `filter`, `append`, and `flatMap` using `foldRight`
        |Because the implementations are incremental, chains of transformations will avoid fully instantiating the intermediate
      data structures.
        |""".stripMargin
  }

  object ex7 {
    val desc =
      """
        Generalize `ones` slightly to the function constant which returns a infinite `Stream` of a given value.
        |""".stripMargin
  }

  object ex8 {
    val desc =
      """
        Write a function that generate an infinite stream of integers, starting from `n`, then `n + 1`, `n + 2` ....
        |""".stripMargin
  }

  object ex9 {
    val desc =
      """
        Write a function fibs that generates the infinite stream of Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8 and so on
        |""".stripMargin
  }

  object ex10 {
    val desc =
      """
        We can write a more general stream building function. It takes an initial state,
        |and a function for producing both the next state and the next value in the generate stream.
        | It is usually called unfold.
        |""".stripMargin
  }

  object ex11 {
    val desc =
      """
        Write fibs, from constant, and ones in terms of unfold
        |""".stripMargin
  }

  object ex12 {
    val desc =
      """
        Use unforl to implement map, take, takeWhile, zip, and zipAll. The zipAll function should continue the traversal
      as long as either stream has more elements - It uses Option to indicate whether each stream has been exhausted.
        |""".stripMargin
  }

  object ex13 {
    val desc =
      """
        Implement startWith using functions you've written. It should check if one Stream is a prefix of another.
        |For instance, Stream( 1, 2 , 3) startsWith Stream( 1, 2) would be true.
        |""".stripMargin
  }

  object ex14 {
    val desc =
      """
        Implement tails using unfold. For a given Stream, tails returns the Stream of suffixes of the input sequence, starting with the original Stream.
        |So, given Stream( 1, 2, 3), it would return Stream( Stream( 1,2,3) , Stream( 2, 3 ) , Stream( 3 ) , Stream.empty).
        |""".stripMargin
  }

  object ex15 {
    val desc =
      """
        Generalize tails to the function scanRight, which is like a fold Right that returns a stream of the intermediate results.
        |""".stripMargin
  }

  def main(args: Array[String]): Unit = {

    ex1.main(args)

  }
}
