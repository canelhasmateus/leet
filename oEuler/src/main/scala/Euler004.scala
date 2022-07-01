import scala.math.Fractional.Implicits.infixFractionalOps
import scala.math.Integral.Implicits.infixIntegralOps
import scala.math.Numeric.Implicits.infixNumericOps
import scala.reflect.Selectable.reflectiveSelectable

object Euler004 {
  //  A palindromic number reads the same both ways.
  //  The largest palindrome made from the product of two 2-digit numbers is
  //  9009 = 91 × 99.
  //
  //  Find the largest palindrome made from the product of two 3-digit numbers.

  def naive(a: Seq[Int], b: Seq[Int]): Option[Int] = {

    val cross = for (elemA <- a; elemB <- b) yield {
      (elemA, elemB)
    }
    val prods = cross.map(_ * _)
    val filts = prods
      .filter(StringUtils.isPalindrome(_))

    return filts.maxOption
  }


}
