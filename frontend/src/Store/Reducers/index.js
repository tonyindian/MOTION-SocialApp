const initialState = {
  user: { things_user_likes: [] },
  user_posts: [],
  token: "",
  posts: [],
  displayPost: false,
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case "SIGNIN":
      return {
        ...state,
        user: action.payload.user,
        token: action.payload.access,
      };
    case "TOKEN":
      return { ...state, token: action.payload };
    case "POSTS":
      return { ...state, posts: action.payload };
    case "FETCHPROFILE":
      return { ...state, user: action.payload };
    case "USERPOSTS":
      return { ...state, user_posts: action.payload };
    default:
      return state;
  }
};

export default reducer;
