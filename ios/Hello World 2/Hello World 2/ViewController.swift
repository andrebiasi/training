//
//  ViewController.swift
//  Hello World 2
//
//  Created by Andre Fernandes on 10/10/19.
//  Copyright © 2019 Andre Fernandes. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var myText: UILabel!
    
    var displayText: String {
        get {
            return myText.text!
        }
        set {
            myText.text = newValue
        }
    }
    
    @IBAction func clickHereTouch(_ sender: UIButton) {
        let greetings = "Hello World"
        displayText = greetings
    }
    
}

