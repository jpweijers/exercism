const UNITS_PER_HOUR: u32 = 221;
const MINUTES_PER_HOUR: u32 = 60;

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let production  =  (speed as u32 * UNITS_PER_HOUR) as f64;
    let efficiency: f64;
    match speed {
        1..=4 => efficiency = 1.0,
        5..=8 => efficiency = 0.9,
        9..=10 => efficiency = 0.77,
        _ => efficiency = 0.0,
    }
    production * efficiency
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    let production_rate = production_rate_per_hour(speed) as u32;
    production_rate / MINUTES_PER_HOUR
}
