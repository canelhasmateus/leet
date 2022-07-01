import scala.math.Ordering.Implicits.infixOrderingOps

object TestUtils {
  def isotonic[T <: Comparable[T], K <: Comparable[K]](f: T => K, n: T, m: T): Boolean = {

    val fn = f(n)
    val fm = f(m)
    return if (n < m) {
      fn <= fm
    }
    else if (n == m) {
      fn == fm
    }
    else if (n > m) {
      fn >= fm
    }
    else {
      false
    }

  }
}
