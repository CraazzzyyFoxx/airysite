import React from 'react';
import classes from './TitleSlide.module.css';
import GreyButton from "../ui/GreyButton/GreyButton";
import GreenButton from "../ui/GreenButton/GreenButton";
import {API_URL} from "../../consts/API";
import {Row, Col} from "antd";

const TitleSlide = () => {
    return (
        <div className={classes.Slide}>
            <div className={classes.SlideInner}>
                <div style={{width: "328px"}}>
                    <h1>Build the best <br/>
                        Discord server!</h1>
                    <h4 style={{color: "#808080"}}>Set up moderation, levels, Twitch notifications, and more with the incredibly easy-to-use control panel!</h4>
                    <div style={{display: "flex", justifyContent: "space-between", marginTop: "28px"}}>
                        <GreenButton onClick={() => {window.open("http://crypto.asuscomm.com/api/v1/add-bot",
                            "popup")}
                        }>
                            Add to Discord
                        </GreenButton>
                        <GreyButton>See feautures</GreyButton>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default TitleSlide;