import java.math.MathContext
import java.util
import scala.collection.mutable.ListBuffer
import scala.math.Ordering.Implicits.infixOrderingOps

object Utils {

  type Pair[+T] = Tuple2[T, T]

  def fib(a: Int = 0, b: Int = 1): Stream[Int] = {
    return (a + b) #:: fib(b, b + a)
  }

  def pairs[T](sequence: Seq[T]): IndexedSeq[Pair[T]] = {
    val s = sequence.size
    for ((i, j) <- indexes(s))
      yield (sequence(i), sequence(j))

  }

  def indexes(size: Int): IndexedSeq[Pair[Int]] = {
    for (i <- Range(0, size);
         j <- Range(i + 1, size))
    yield (i, j)
  }

  def sumOfProgression(ceil: BigInt, step: BigInt = 1): BigInt = {
    // TODO: Change method name.
    val numberOfSteps: BigInt = (ceil - 1) / step
    val sumOfSteps: BigInt = (numberOfSteps * (numberOfSteps + 1)) / 2
    return step * sumOfSteps
  }

  def lazyRange(start: BigInt = BigInt(0)): LazyList[BigInt] = {
    return start #:: lazyRange(start + 1)
  }

  def ceilSqrt(n: BigInt): BigInt = {

    val root = scala.math.sqrt(n.toDouble)

    return BigDecimal(root).setScale(0, BigDecimal.RoundingMode.HALF_UP).toBigInt
  }


}
