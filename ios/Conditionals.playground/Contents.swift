import UIKit

var number = 3

if number % 2 == 0 {
    print("The number \(number) is even")
}
else {
    print("The number \(number) is odd")
}

var num1: Int8 = 1
var num2: Int32 = 1
print(num1 == num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 != num2)

var message = num1 == 1 ? "Number is 1" : "Number is NOT 1"

if num1 > num2 {
    print("greater")
}
else if num1 < num2 {
    print("less")
}
else {
    print("equal")
}

var statusCode = 404
var errorMessage = ""
switch statusCode {
case 400:
    errorMessage = "Bad request"
case 401:
    errorMessage = "Unauthorised"
case 403:
    errorMessage = "Forbidden"
case 404:
    errorMessage = "Not found"
default:
    errorMessage = "None"
}
print("\(statusCode) - \(errorMessage)")

switch statusCode {
case 400, 401, 403, 404:
    print("some error")
    fallthrough
default:
    print("please review and try again")
}

let a = 20
switch a {
case 1...10:
    print("between 1 and 10")
case 11...20:
    print("between 11 and 20")
default:
    print("another range")
}

let b = 0
switch b {
case 1:
    print("one")
case 2:
    print("two")
case let otherNumber where otherNumber == 0:
    print("\(otherNumber) is invalid")
default:
    print("not spelled")
}
