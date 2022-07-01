import scala.annotation.tailrec

object Examples extends App {


  def fib(n: Int): Int = {

    @tailrec
    def loop(n: Int, prev: Int, cur: Int): Int = {
      if n <= 0
      then
        prev
      else
        loop(n - 1, cur, prev + cur)
    }

    loop(n, 0, 1)
  }


  def tail[T](list: List[T]): List[T] =
    return list match {
      case Nil => Nil
      case x :: xs => xs
    }

  @tailrec
  def drop[T](list: List[T], n: Int): List[T] =
    n match {
      case 0 => list
      case _ => drop(tail(list), n - 1)
    }

  @tailrec
  def dropWhile[T](list: List[T], predicate: T => Boolean):  List[T] =
    list match {
      case Nil => Nil
      case x :: xs => if (predicate(x)) {
        list
      } else {
        dropWhile(xs, predicate)
      }

    }

  def setHead[T](list: List[T], newHead: T): List[T] = {
    list match {
      case Nil => Nil
      case oldHead :: tail => newHead :: tail
    }
  }

//  print(Range(0, 10).map(fib))


  def foldRight[A,B](l: List[A], z: B)(f: (A, B) => B): B =
    l match {
      case Nil => z
      case x :: xs => f(x, foldRight(xs, z)(f))
    }

  def passNilCons(): Unit = {
    foldRight( List( 1 , 2 , 3 ) , Nil:List[Int])( _ :: _)
  }

  def length[A]( l  : List[A] ) : Int =
    foldRight( l  , 0)( ( a , acc ) => 1 + acc)

  def foldLeft[A,B](l: List[A], z: B)(f: (B, A) => B): B =
    l match {
      case Nil => z
      case head :: tail => foldLeft( tail, f(z , head) ) ( f )

    }

  println(passNilCons())
  println(length( List( 1 , 2, 3 , 3 , 4)))

//

}
