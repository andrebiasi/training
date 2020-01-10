//
//  ViewController.swift
//  Hello World
//
//  Created by Andre Fernandes on 9/10/19.
//  Copyright © 2019 Andre Fernandes. All rights reserved.
//

import UIKit

enum modes{
    case notSet
    case addition
    case subtraction
}

class ViewController: UIViewController {
    @IBOutlet weak var myLabel: UILabel!
    @IBOutlet weak var myLabel2: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        var mode: modes = .notSet
        mode = .addition
        
        let myText = "Hello World"
        let myNumber = 123
        myLabel.text = myText
        myLabel2.text = "\(myNumber)"
        
    }


}

