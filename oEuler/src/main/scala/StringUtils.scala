object StringUtils {


  def isPalindrome[T <: Serializable](candidate: T): Boolean = {
    return candidate.toString == candidate.toString.reverse
  }
}

