name := "euler"

version := "0.1"

scalaVersion := "3.0.2"


libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.10" % "test"
libraryDependencies += "org.scalatestplus" %% "scalacheck-1-15" % "3.2.9.0" % "test"
libraryDependencies += "com.storm-enroute" %% "scalameter" % "0.21-SNAPSHOT" % "bench"


enablePlugins(JmhPlugin)
