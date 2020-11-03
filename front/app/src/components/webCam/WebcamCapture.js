import React, { useRef, useCallback, useState, Component } from "react";
import Webcam from "react-webcam";
import axios from "axios"
import "./WebcamCapture.css"


const videoConstraints = {
    //width: 1280,
    width: 10,
    //height: 720,
    height: 10,
    facingMode: "user"
};

const WebcamCapture = () => {
    console.log("start");
    const webcamRef = React.useRef(null);
    const canvasRef = React.useRef(null);

    // const [color, setColor] = React.useState('');
    // const [check, setCheck] = React.useState(0);
    const color = "yellow";
    const check = 0;

    const onStart = () => {
        //check = 1;
    }

    const onStop = () => {
        //check = 0;
    } 

    function drawImge() {
        const video = webcamRef.current;
        const canvas = canvasRef.current;
        if (video && canvas) {
            var ctx = canvas.getContext('2d');

            canvas.width = video.video.videoWidth;
            canvas.height = video.video.videoHeight;

            // We want also the canvas to display de image mirrored
            ctx.translate(canvas.width, 0);
            ctx.scale(-1, 1);
            ctx.drawImage(video.video, 0, 0, canvas.width, canvas.height);
            ctx.scale(-1, 1);
            ctx.translate(-canvas.width, 0);

            // var faceArea = 300;
            // var pX = canvas.width / 2 - faceArea / 2;
            // var pY = canvas.height / 2 - faceArea / 2;
            //ctx.rect(pX, pY, faceArea, faceArea);
            
            var radius = 0;
            var centerX = canvas.width/2;
            var centerY = canvas.height/2;
            if (canvas.width > canvas.height){radius = canvas.height * 21 / 100}
            else {radius = canvas.width * 21 / 100}
            radius = radius*90/100;
            ctx.arc(centerX, centerY, radius, 0, Math.PI * 2)
            ctx.lineWidth = "3";
            ctx.strokeStyle = color;
            ctx.stroke();
            //capture();
            setTimeout(drawImge, 100);
        }
    }
    setTimeout(drawImge, 100);


    // function videoCapture(){
    //     if(check == 1){capture();}
    //     else console.log("out")
    //     console.log(check);
    //     setTimeout(videoCapture, 3000);
    // }
    // setTimeout(videoCapture, 3000);

    const capture = React.useCallback(
        () => {
            //const imageSrc = webcamRef.current.getScreenshot();
            const imageSrc = webcamRef.current.getScreenshot({width: 1920, height: 1080});

            fetch("http://localhost:8000/", {
                method: "POST",
                body: JSON.stringify({
                    "image": imageSrc
                }),
            })
                .then((res) => res.json())
                .then((response) => {
                    console.log(response);
                });
        },
        [webcamRef]
    );

    return (
        <div className="WebcamCapture">
            <Webcam
                audio={false}
                //height={720}
                height={200}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                //width={1280}
                mirrored
                width={200}
            //videoConstraints={videoConstraints}
            />
            <canvas ref={canvasRef} style={{ width: 200, height: 150 }} />
            <button onClick={capture}>start</button>
            <button onClick={onStop}>stop</button>
        </div>
    );
};


export default WebcamCapture;