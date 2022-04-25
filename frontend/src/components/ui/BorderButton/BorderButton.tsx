import React, {FC} from 'react';
import classes from './BorderButton.module.css';

interface BorderButtonProps {
    id?: string
    children: React.ReactChild | React.ReactNode
}


const BorderButton: FC<BorderButtonProps> = ({
                                         id,
                                         children}) => {
    return (
        <button className={classes.myBtn}>
            {children}
        </button>
    );
};


export default BorderButton;