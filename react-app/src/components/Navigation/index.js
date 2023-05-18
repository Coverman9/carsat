import React from "react";
import { NavLink } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import { Link } from "react-router-dom";
import "./Navigation.css";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <div className="main-navbar">
      <ul>
        <li>
          <NavLink exact to="/">
            Home
          </NavLink>
        </li>
        {isLoaded && (
          <>
            <li>
              <ProfileButton user={sessionUser} />
            </li>
            <div>
              {sessionUser && (
                <>
                  <Link to="/cars">
                    <button>All Cars</button>
                  </Link>
                  <Link to="/cars/new">
                    <button>Add a Car</button>
                  </Link>
				  <Link to={`/profile/${sessionUser.id}`}>
				  	<button>Profile</button>
				  </Link>
                </>
              )}
            </div>
          </>
        )}
      </ul>
    </div>
  );
}

export default Navigation;
