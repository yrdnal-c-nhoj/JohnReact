import PropTypes from 'prop-types';

function UserGreeting(props) {

    const welcomeMessage = <h2 className="welcome-message">
        Hello, {props.username}
    </h2>

    const loginPrompt = <h2 className="login-orompt">
        log in please
    </h2>

    return (props.isLoggedIn ? welcomeMessage : loginPrompt);
}
UserGreeting.prototype = {
    isLoggedIn: PropTypes.bool,
    username: PropTypes.string,
}
UserGreeting.defaultProps = {
    isLoggedIn: true,
    username: "Guest",
}

export default UserGreeting