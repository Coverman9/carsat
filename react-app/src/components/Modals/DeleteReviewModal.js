import "./Modals.css"
import { useModal } from "../../context/Modal"
import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"
import { deleteReviewThunk } from "../../store/reviews"


const DeleteReviewModal = ({review}) => {
    const { closeModal } = useModal()
    const dispatch = useDispatch()
    const history = useHistory()

    const confirmDelete = async () => {
        await dispatch(deleteReviewThunk(review.id))
        closeModal()
    }
    return (
        <>
            <h2>Delete Car</h2>
            <p>Are u sure you want remove your car?</p>
            <button onClick={confirmDelete}>Yes</button>
            <button onClick={closeModal}>No</button>
        </>
    )
}


export default DeleteReviewModal
