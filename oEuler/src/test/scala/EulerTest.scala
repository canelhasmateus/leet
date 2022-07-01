import Euler001.*
import TestUtils.isotonic
import org.scalacheck.Arbitrary.arbitrary
import org.scalacheck.Prop.forAll
import org.scalacheck.{Gen, Properties}
import org.scalatest.*
import org.scalatest.funsuite.AnyFunSuite
import org.scalatest.matchers.should.Matchers
import org.scalatest.propspec.AnyPropSpec

import scala.math.Ordering.Implicits.infixOrderingOps


class EulerTest extends EulerTestSpec {


  //region init
  val positiveInteger: Gen[Int] = Gen.posNum
  //endregion

  test("Euler 1") {

    withClue("Known results") {
      assert(Euler001.fast(10) == 23)
      assert(Euler001.fast(1000) == 233168)
    }

    withClue("Fast and naive equivalence") {
      forAll(positiveInteger) { (n: Int) =>
        assert(Euler001.fast(n) == Euler001.naive(n))
      }
    }

    withClue("Isotonicity") {

      forAll(positiveInteger, positiveInteger) { (n: Int, m: Int) =>
        val f: BigInt => BigInt = Euler001.fast(_, List(3, 5))
        assert(isotonic(f, n, m))
      }

    }

  }

  test("Euler 2") {

    withClue("Known results") {
      assert(Euler002.naive(4_000_000) == 4613732)
    }

    withClue("Fast and naive equivalence") {
      forAll(positiveInteger) { (n: Int) =>
        assert(Euler002.naive(n) == Euler002.fast(n))
      }
    }

    withClue("Isotonicity") {
      forAll(positiveInteger, positiveInteger) { (n: Int, m: Int) =>
        val f = Euler002.fast
        assert(isotonic(f, n, m))
      }

    }
  }

  test("Euler 3") {

    withClue("Known Results") {

      //      assert(Euler003.naive(13195) == 29)
      assert(Euler003.naive(600_851_475_143L) == 6857)
    }
  }


  test("Euler 4") {

    withClue("Known results") {

      val set = List.range(1, 100)
      assert(Euler004.naive(set, set) == Some(9009))
      val triSet = List.range(1, 1000)
      info(Euler004.naive(triSet, triSet).toString)
    }
  }
}
