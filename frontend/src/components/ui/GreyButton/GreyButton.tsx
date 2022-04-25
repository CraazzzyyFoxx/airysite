import React, {FC} from 'react';
import classes from './GreyButton.module.css';

interface MyButtonProps {
    id?: string
    children: React.ReactChild | React.ReactNode
}


const GreyButton: FC<MyButtonProps> = ({id,
                                           children}) => {
    return (
        <button className={classes.myBtn}>
            {children}
        </button>
    );
};

export default GreyButton;