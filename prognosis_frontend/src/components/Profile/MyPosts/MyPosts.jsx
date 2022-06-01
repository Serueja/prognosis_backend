import React from 'react';
import { addPostActionCreator, updateNewPostTextActionCreator } from '../../../redux/profile-reducer';
import s from './MyPosts.module.css';
import Posts from './Posts/Posts';

const MyPosts = (props) => {

    let postsElements = props.posts.map(p => <Posts message={p.message} id={p.id} />);
    
    let newPostElement = React.createRef();

    let addPost = () => {
        props.addPost();
    };

    let onPostChange = () => {
        let text = newPostElement.current.value;
        props.updateNewPostText(text);
    }

    return <div className={s.postsBlock}>
        <h3>My posts</h3>
        <div>
            <div>
                <textarea onChange={onPostChange} 
                ref={newPostElement}
                placeholder = 'Write a post'
                    value={props.newPostText} />
            </div>

            <div>
                <button className={s.addPost} onClick={addPost} >Add post</button>
            </div>

        </div>
        <div className={s.posts}>
            {postsElements}
        </div>
    </div>
}

export default MyPosts;