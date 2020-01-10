import UIKit

print("Max Int value is \(Int.max)")
print("Min Int value is \(Int.min)")

print("Max Int8 value is \(Int8.max)")
print("Min Int8 value is \(Int8.min)")

print("Max Int16 value is \(Int16.max)")
print("Min Int16 value is \(Int16.min)")

print("Max Int32 value is \(Int32.max)")
print("Min Int32 value is \(Int32.min)")

print("Max Int64 value is \(Int64.max)")
print("Min Int64 value is \(Int64.min)")

print("Max UInt value is \(UInt.max)")
print("Min UInt value is \(UInt.min)")

print("Max UInt8 value is \(UInt8.max)")
print("Min UInt8 value is \(UInt8.min)")

print("Max UInt16 value is \(UInt16.max)")
print("Min UInt16 value is \(UInt16.min)")

print("Max UInt32 value is \(UInt32.max)")
print("Min UInt32 value is \(UInt32.min)")

print("Max UInt64 value is \(UInt64.max)")
print("Min UInt64 value is \(UInt64.min)")


var x = 1
print(x)
x *= 2
print(x)
x /= 2
print(x)
x -= 1
print(x)


let y: Int8 = 120
// let z = y + 10
let z = y &+ 10 // overflow operator
print(z)

let a: Int8 = 1
let b: Int16 = 2
// let c = a + b
let c = Int16(a) + b

let d1 = 1.1 // Implicitly Double
let d2: Double = 1.1 // Explicitly Double
let f1: Float = 1.1
print(d1)
print(d2)
print(d1 == d2)
print(Float(d1))
print(f1)
print(Double(f1))
print(d1 == Double(f1))
