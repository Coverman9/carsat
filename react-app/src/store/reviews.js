const ALL_REVIEWS_OF_CAR = "reviews/ALL_REVIEWS_OF_CAR";
const ALL_REVIEWS_OF_USER = "reviews/ALL_REVIEWS_OF_USER";
const CREATE_REVIEW = "reviews/CREATE_REVIEW";
const UPDATE_REVIEW = "reviews/UPDATE_REVIEW";
const DELETE_REVIEW = "reviews/DELETE_REVIEW";

const allCarReviewsAction = (reviews) => ({
  type: ALL_REVIEWS_OF_CAR,
  reviews,
});

const allUserReviewsAction = (reviews) => ({
  type: ALL_REVIEWS_OF_USER,
  reviews,
});

const createReviewAction = (review) => ({
  type: CREATE_REVIEW,
  review,
});

const updateReviewAction = (review) => ({
  type: UPDATE_REVIEW,
  review,
});

const deleteReviewAction = (reviewId) => ({
  type: DELETE_REVIEW,
  reviewId,
});

///-------------------THUNK-------------------------

export const getAllCarReviewsThunk = (carId) => async (dispatch) => {

  const res = await fetch(`/api/reviews/car/${carId}`);
  const reviews = await res.json();

  await dispatch(allCarReviewsAction(reviews));
};

export const getAllUserReviewsThunk = (userId) => async (dispatch) => {
  const res = await fetch(`/api/reviews/user/${userId}`);
  const reviews = await res.json();

  await dispatch(allUserReviewsAction(reviews));
};

export const createReviewThunk = (_review) => async (dispatch) => {
  const { review, stars, carId } = _review;
  const res = await fetch(`/api/reviews/${carId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      review,
      stars,
    }),
  });

  if (res.ok) {
    const newReview = await res.json();
    dispatch(createReviewAction(newReview));
    return newReview;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const updateReviewThunk = (_review) => async (dispatch) => {
  const { review, stars, reviewId } = _review;
  const res = await fetch(`/api/reviews/${reviewId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      review,
      stars,
    }),
  });

  if (res.ok) {
    const newReview = await res.json();
    dispatch(updateReviewAction(newReview));
    return newReview;
  } else {
    const errors = await res.json();
    return errors;
  }
};

export const deleteReviewThunk = (reviewId) => async (dispatch) => {
  const res = await fetch(`/api/reviews/${reviewId}`, {
    method: "DELETE",
  });

  if (res.ok) {
    dispatch(deleteReviewAction(reviewId));
  } else {
    const errors = await res.json();
    return errors;
  }
};
///------------------REDUCERS--------------------------

const initialState = {};

const reviews = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case ALL_REVIEWS_OF_CAR:
      action.reviews.reviews.forEach((review) => (newState[review.id] = review));
      return newState;
    case ALL_REVIEWS_OF_USER:
      action.reviews.reviews.forEach((review) => (newState[review.id] = review));
      return newState;
    case CREATE_REVIEW:
      newState = { ...state };
      newState[action.review.id] = action.review;
      return newState;
    case UPDATE_REVIEW:
      return { ...state, [action.review.id]: action.review };
    case DELETE_REVIEW:
      newState = { ...state };
      delete newState[action.reviewId];
      return newState;
    default:
      return state;
  }
};

export default reviews;
