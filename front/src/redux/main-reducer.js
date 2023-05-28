import { createStore } from 'redux';


const initialState = {
    data: ""
}

const mainPageDataReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'SET_MAIN_PAGE_DATA':
            return { ...state, data: action.payload };
        default:
            return state;
    }
}

const store = createStore(mainPageDataReducer);

export default store;