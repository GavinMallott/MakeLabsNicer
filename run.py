"""
Author: Gavin Mallott
Created: October 3, 2017
Lasted Edited: October 10, 2017
"""


from flask import Flask, render_template
from locate_p import AssignmentData


app = Flask('MakeLabsNicer')

@app.route('/')
def index():
    return render_template('index.html', variable='Template Home')


@app.route('/lab0/')
def lab0():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab0.html')

    return render_template('labs.html', lab_number='Lab 0', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab1/')
def lab1():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab1.html')
    
    return render_template('labs.html', lab_number='Lab 1', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab2/')
def lab2():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab2.html')
    
    return render_template('labs.html', lab_number='Lab 2', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab3/')
def lab3():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab3.html')
    
    return render_template('labs.html', lab_number='Lab 3', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab4/')
def lab4():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab4.html')
    
    return render_template('labs.html', lab_number='Lab 4', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab5/')
def lab5():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab5.html')
    
    return render_template('labs.html', lab_number='Lab 5', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab6/')
def lab6():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab6.html')
    
    return render_template('labs.html', lab_number='Lab 6', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab7/')
def lab7():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab7.html')
    
    return render_template('labs.html', lab_number='Lab 7', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab8/')
def lab8():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab8.html')
    
    return render_template('labs.html', lab_number='Lab 8', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)


@app.route('/lab9/')
def lab9():
    lab = AssignmentData('http://www.ics.uci.edu/~kay/courses/31/hw/lab9.html')
    
    return render_template('labs.html', lab_number='Lab 9', prep=lab.p_prep, lab=lab.p_lab, turnin_text=lab.p_turnin, start=lab.p_start[0], end=lab.p_end)

if __name__ == '__main__':
    app.run()