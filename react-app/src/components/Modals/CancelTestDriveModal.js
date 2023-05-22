import "./Modals.css"
import { useModal } from "../../context/Modal"
import { useDispatch } from "react-redux"
import { useHistory } from "react-router-dom"
import { cancelTestdriveThunk } from "../../store/testdrives"


const CancelTestdriveModal = ({testdrive}) => {
    const { closeModal } = useModal()
    const dispatch = useDispatch()
    const history = useHistory()

    const confirmCancel = async () => {
        await dispatch(cancelTestdriveThunk(testdrive.id))
        closeModal()
    }
    return (
        <>
            <h2>Cancel Test drive</h2>
            <p>Are you sure you want to cancel testdrive?</p>
            <button onClick={confirmCancel}>Yes</button>
            <button onClick={closeModal}>No</button>
        </>
    )
}


export default CancelTestdriveModal
