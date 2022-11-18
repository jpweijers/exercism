/// various log levels
#[derive(Clone, PartialEq, Eq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug,
}
/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    let log_message;
    match level {
        LogLevel::Info => log_message = info(message),
        LogLevel::Warning => log_message = warn(message),
        LogLevel::Error => log_message = error(message),
        LogLevel::Debug => log_message = debug(message),
    }
    log_message
}
pub fn info(message: &str) -> String {
    format!("[INFO]: {}", message.to_string())
}
pub fn warn(message: &str) -> String {
    format!("[WARNING]: {}", message.to_string())
}
pub fn error(message: &str) -> String {
    format!("[ERROR]: {}", message.to_string())
}
pub fn debug(message: &str) -> String {
    format!("[DEBUG]: {}", message.to_string())
}
