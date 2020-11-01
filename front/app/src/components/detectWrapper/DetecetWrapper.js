import React, { Component } from 'react';
import WebcamCapture from '../webCam/WebcamCapture'
//import './DetectWrapper.css'

class DetectWrapper extends Component{
    render(){
        return(
            <div className="DetectWrapper">
                <WebcamCapture></WebcamCapture>
            </div>
        );
    };
}

export default DetectWrapper;