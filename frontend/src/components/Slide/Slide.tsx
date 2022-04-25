import React from 'react';
import classes from './Slide.module.css';
import GreyButton from "../ui/GreyButton/GreyButton";
import GreenButton from "../ui/GreenButton/GreenButton";

const Slide = () => {
    return (
        <div className={classes.Slide}>
            <div className={classes.SlideInner}>
                <div style={{width: "328px"}}>
                    <h1>Create the best discord server with Airy</h1>
                    <h4 style={{color: "#808080"}}>Set up moderation, levels, Twitch notifications, and more with the incredibly easy-to-use control panel!</h4>
                    <div style={{display: "flex", justifyContent: "space-between", marginTop: "28px"}}>
                        <GreenButton>Add to Discord</GreenButton>
                        <GreyButton>See feautures</GreyButton>
                    </div>
                </div>
                <img src="img/img420x332.png" style={{objectFit: "contain"}}/>
            </div>
        </div>
    )
};

export default Slide;