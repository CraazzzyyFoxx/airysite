import React, {FC} from 'react';
import classes from './TinySlide.module.css';

interface TinySlideProps {
    text: React.ReactChild
}



const TinySlide: FC<TinySlideProps> = ({text}) => {
    return (
        <div className={classes.TinySlide}>
            <h2>{text}</h2>
        </div>
    );
};

export default TinySlide;