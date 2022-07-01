import java.util
import scala.collection.mutable
import scala.math.{ceil, pow, sqrt}

object Euler003 {

  //  The prime factors of 13195 are 5, 7, 13 and 29.
  //
  //  What is the largest prime factor of the number 600851475143 ?


  def naive(number: Long): Long = {

    val bound = ceil(sqrt(number))
    // TODO:  Can optimize it further, via better wheels.
    return PrimeUtils.primeStream(PrimeUtils.primeWheel())
      .takeWhile(_ <= bound)
      .filter(PrimeUtils.isDivisor(number, _))
      .maxOption.getOrElse(number)
  }
  
}

