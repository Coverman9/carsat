import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Cars from "./components/Cars";
import CarDetail from "./components/CarDetail";
import AddCar from "./components/AddCar";
import Profile from "./components/Profile";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route exact path="/login" >
            <LoginFormPage />
          </Route>
          <Route exact path="/signup">
            <SignupFormPage />
          </Route>
          <Route exact path="/cars">
            <Cars />
          </Route>
          <Route exact path="/cars/new">
            <AddCar />
          </Route>
          <Route exact path="/cars/:carId">
            <CarDetail/>
          </Route>
          <Route exact path="/profile/:profileId">
            <Profile />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
