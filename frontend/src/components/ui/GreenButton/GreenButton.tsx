import React, {FC} from 'react';
import classes from './GreenButton.module.css';
import {Button} from "antd";

interface GreenButtonProps {
    id?: string
    children: React.ReactChild | React.ReactNode
    style?: any
    onClick?: () => any
}


const GreenButton: FC<GreenButtonProps> = (props) => {
    return (
        <button className={classes.myBtn} {...props}>
            {props.children}
        </button>
    );
};

export default GreenButton;