import React from 'react';
import s from './Posts.module.css';

const Posts = (props) => {

    return <div className={s.item}>

        {props.message}
        <div>
        </div>
    </div>
}

export default Posts;