import scala.annotation.tailrec
import scala.math.Ordering.Implicits.infixOrderingOps

object Teste extends App {


  def quicksort[T: Ordering](arg: List[T]): List[T] =

    return arg match
      case Nil => Nil
      case head :: tail => {
        val lesser = tail.filter(_ < head)
        val greater = tail.filter(_ >= head)
        quicksort(lesser) ::: head :: quicksort(greater)
      }



  val aList = List(44, 1, 3, 2, 5)
  val sorted = Teste quicksort aList
  println(aList)
  println(sorted)

  def byName( a : => Long ): Unit = {
    println( a )
    println( a )
  }

  byName( System.nanoTime() )
}
