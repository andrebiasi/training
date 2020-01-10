import UIKit

let error = (404, "Not Found")
print(error.0)
print(error.1)

let person = (name: "Andre", age: 37, pet: "Sam")
print(person.name)
print(person.age)
print(person.pet)

let firstErrorCode = 200
let secondErrorCode = 200
let errorCodes = (firstErrorCode, secondErrorCode)

switch errorCodes {
case (404, 404):
    print("No items found")
case (404, _):
    print("First item not found")
case(_, 404):
    print("Second item not found")
default:
    print("All items found")
}


let age = 25

// bad way
switch age {
case 18...35:
    print("cool age")
default:
    break
}

// good way
if case 18...35 = age {
    print("cool age")
}


