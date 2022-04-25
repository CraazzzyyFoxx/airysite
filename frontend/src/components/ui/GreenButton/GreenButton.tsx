import React, {FC} from 'react';
import classes from './GreenButton.module.css';

interface GreenButtonProps {
    id?: string
    children: React.ReactChild | React.ReactNode
    style?: any
    onClick?: () => any
}


const GreenButton: FC<GreenButtonProps> = ({id,
                                               children,
                                               onClick,
                                               style}) => {
    return (
        <button className={classes.myBtn} style={style} onClick={onClick}>
            {children}
        </button>
    );
};

export default GreenButton;