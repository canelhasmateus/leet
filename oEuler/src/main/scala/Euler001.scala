import Utils.{Pair, sumOfProgression}

object Euler001 {

  //If we list all the natural numbers below 10 that are multiples of 3 or 5,
  // we get 3, 5, 6 and 9. The sum of these multiples is 23.
  //
  //Find the sum of all the multiples of 3 or 5 below 1000.

def naive(ceil: BigInt, factors: List[BigInt] = List(3, 5)): BigInt = {
      type Predicate[T] = T => Boolean

      val functions: List[Predicate[BigInt]] = factors.map(f => { (n) => n % f == 0 })

      val isInteresting = functions.reduce((f, g) => { n => f(n) || g(n) })
      val range: Seq[BigInt] = List.range(0, ceil)
          return range.filter(isInteresting).reduce(_ + _)

}

  def fast(ceil: BigInt, factors: List[BigInt] = List(3, 5)): BigInt = {

    val multiples = Utils.pairs(factors.distinct).map((x: Pair[BigInt]) => x._1 * x._2)

    val sumOfFactors = factors.map(Utils.sumOfProgression(ceil, _)).sum

    val sumOfMultiples = multiples.map(Utils.sumOfProgression(ceil, _)).sum

    return sumOfFactors - sumOfMultiples
  }


}
