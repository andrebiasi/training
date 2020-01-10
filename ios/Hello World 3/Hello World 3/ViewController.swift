//
//  ViewController.swift
//  Hello World 3
//
//  Created by Andre Fernandes on 19/10/19.
//  Copyright © 2019 Andre Fernandes. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var displayLabel: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        displayLabel.text = "Hello World.\nThis is a test!!!"
        displayLabel.sizeToFit()
    }


}

