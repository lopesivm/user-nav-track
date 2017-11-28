var server_addr = null;

function getUserUUID() {
    return localStorage.getItem('tracker-uuid');
}

// Extracted from: https://stackoverflow.com/questions/105034/create-guid-uuid-in-javascript
// The reason for copying the code was to find an RFC compliant, pure JS, uuid generator, to ensure uniqueness
function setUserUUID() {
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
    localStorage.setItem('tracker-uuid', uuid);
    return uuid;
}

function sendTracking(server_addr, uuid, title, url, datetime) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', server_addr + '/user/' + uuid + '/track');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Log below is purely for visual purposes on the scope of this exercise. In a real world scenario it
            // would be better not to print each page tracked.
            console.log('Successfully tracking page ' + title + ' at ' + url + ' for user ' + uuid);
        }
    };
    xhr.send(JSON.stringify({
        title: title,
        url: url,
        datetime: datetime
    }));
}

function registerEmail() {
    var email = document.getElementById("emailUNT").value;
    var uuid = getUserUUID();
    var xhr = new XMLHttpRequest();
    xhr.open('POST', server_addr + '/user/' + uuid + '/email');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Successfully registered email ' + email + ' for user ' + uuid);
        }
    };
    xhr.send(JSON.stringify({
        email: email
    }));
}

function UNT(force_addr) {
    var default_server_addr = 'https://user-navigation-tracking.herokuapp.com';
    server_addr = (typeof force_addr !== 'undefined' && force_addr) ? force_addr : default_server_addr;
    var title = document.title;
    var url = document.location.href;
    var uuid = getUserUUID() ? getUserUUID() : setUserUUID();
    var datetime = Date.now();
    sendTracking(server_addr, uuid, title, url, datetime);
}