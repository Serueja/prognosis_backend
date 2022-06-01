import profileReducer from "./profile-reducer";
import dialogsReducer from "./dialogs-reducer";
import sidebarReducer from "./sidebar-reducer";

let store = {
    _state: {
        profilePage: {
            posts: [
                { id: 1, message: 'Сегодня выбил леончика!))' },
                { id: 2, message: 'ребят вам тоже штолня не нрав((?' }
            ],
            newPostText: ""

        },
        dialogsPage: {
            messages: [
                { id: 1, message: 'Го в бравлик щас' },
                { id: 2, message: 'НЕ УСПЕЛ КУПИТЬ АКЦИЮ' },
                { id: 3, message: 'Штольня bebe((' },
            ],

            dialogs: [
                { id: 1, name: 'Dmitry' },
                { id: 2, name: 'Nikita' },
                { id: 3, name: 'Misha' },
                { id: 4, name: 'Artem' },
                { id: 5, name: 'Vlad' },
            ],
            newMessageBody: ""
        },
        sidebar: {}

    },

    
    _callSubscriber() {
        console.log('state was changed');
    },
    getState() {
        return this._state;
    },
    subscribe(observer) {
        this._callSubscriber = observer;
    },

    dispatch(action) {

        this._state.profilePage  = profileReducer(this._state.profilePage, action);
        this._state.dialogsPage = dialogsReducer(this._state.dialogsPage, action);
        this._state.sidebar = sidebarReducer(this._state.sidebar, action);

        this._callSubscriber(this._state);
        
    },
}
 
export default store;