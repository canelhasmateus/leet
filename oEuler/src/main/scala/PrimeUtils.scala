import scala.math.*

object PrimeUtils {

  opaque type Wheel = () => Long

  def isDivisor(number: Long, candidate: Long): Boolean = {
    return number % candidate == 0

  }

  def isPrime(number: Long): Boolean = {
    val bound = ceil(sqrt(number))
    return wheelStream(2, primeWheel())
      .takeWhile(_ <= bound)
      .filter(isDivisor(number, _))
      .size == 0
  }

  def primeStream(stepper: Wheel): LazyList[Long] = {
    return wheelStream(2, primeWheel()).filter(isPrime)
  }

  def wheelStream(start: Long = 0, wheel: Wheel): LazyList[Long] = {
    val stepSize = wheel()
    start #:: wheelStream(start + stepSize, wheel)
  }

  def primeWheel(factors: Long*): Wheel = {

    var i = 0

    val cycle: Seq[Long] = List(4, 2, 4, 2, 4, 6, 2, 6)
    return () => {
      i += 1
      if (i > 3) cycle((i - 4) % cycle.size)
      else if (i == 3) 2
      else if (i == 2) 2
      else 1
    }


  }
}