const ADD_POST = 'ADD-POST';
const UPDATE_NEW_POST_TEXT = 'UPDATE-NEW-POST-TEXT';


const initialState =  {
    posts: [
        { id: 1, message: 'Сегодня выбил леончика!))' },
        { id: 2, message: 'ребят вам тоже штолня не нрав((?' }
    ],
    newPostText: "lol "

};


const profileReducer = (state = initialState, action) => {
    switch (action.type) {

        case ADD_POST: {
            let newPost = {
                id: 3,
                message: state.newPostText,
                likesCount: 0
            };
            let stateCopy = { ...state };
            stateCopy.posts = [...state.posts];
            stateCopy.posts.push(newPost);
            stateCopy.newPostText = '';
            return stateCopy;

        }

        case UPDATE_NEW_POST_TEXT: {
            let stateCopy = { ...state };
            stateCopy = [...state.posts];
            stateCopy.newPostText = action.newText;
            return stateCopy;

        }
        default:
            return state;
    }
}
export const addPostActionCreator = () => ({ type: ADD_POST })
export const updateNewPostTextActionCreator = (text) =>
    ({ type: UPDATE_NEW_POST_TEXT, newText: text })

export default profileReducer;