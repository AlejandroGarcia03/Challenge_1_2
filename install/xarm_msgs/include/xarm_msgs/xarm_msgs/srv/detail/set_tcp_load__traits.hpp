// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from xarm_msgs:srv/SetTcpLoad.idl
// generated code does not contain a copyright notice

#ifndef XARM_MSGS__SRV__DETAIL__SET_TCP_LOAD__TRAITS_HPP_
#define XARM_MSGS__SRV__DETAIL__SET_TCP_LOAD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "xarm_msgs/srv/detail/set_tcp_load__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace xarm_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetTcpLoad_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: weight
  {
    out << "weight: ";
    rosidl_generator_traits::value_to_yaml(msg.weight, out);
    out << ", ";
  }

  // member: center_of_gravity
  {
    if (msg.center_of_gravity.size() == 0) {
      out << "center_of_gravity: []";
    } else {
      out << "center_of_gravity: [";
      size_t pending_items = msg.center_of_gravity.size();
      for (auto item : msg.center_of_gravity) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetTcpLoad_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: weight
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "weight: ";
    rosidl_generator_traits::value_to_yaml(msg.weight, out);
    out << "\n";
  }

  // member: center_of_gravity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.center_of_gravity.size() == 0) {
      out << "center_of_gravity: []\n";
    } else {
      out << "center_of_gravity:\n";
      for (auto item : msg.center_of_gravity) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetTcpLoad_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace xarm_msgs

namespace rosidl_generator_traits
{

[[deprecated("use xarm_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const xarm_msgs::srv::SetTcpLoad_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  xarm_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use xarm_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const xarm_msgs::srv::SetTcpLoad_Request & msg)
{
  return xarm_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<xarm_msgs::srv::SetTcpLoad_Request>()
{
  return "xarm_msgs::srv::SetTcpLoad_Request";
}

template<>
inline const char * name<xarm_msgs::srv::SetTcpLoad_Request>()
{
  return "xarm_msgs/srv/SetTcpLoad_Request";
}

template<>
struct has_fixed_size<xarm_msgs::srv::SetTcpLoad_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<xarm_msgs::srv::SetTcpLoad_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<xarm_msgs::srv::SetTcpLoad_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace xarm_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetTcpLoad_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: ret
  {
    out << "ret: ";
    rosidl_generator_traits::value_to_yaml(msg.ret, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetTcpLoad_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ret
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ret: ";
    rosidl_generator_traits::value_to_yaml(msg.ret, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetTcpLoad_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace xarm_msgs

namespace rosidl_generator_traits
{

[[deprecated("use xarm_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const xarm_msgs::srv::SetTcpLoad_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  xarm_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use xarm_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const xarm_msgs::srv::SetTcpLoad_Response & msg)
{
  return xarm_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<xarm_msgs::srv::SetTcpLoad_Response>()
{
  return "xarm_msgs::srv::SetTcpLoad_Response";
}

template<>
inline const char * name<xarm_msgs::srv::SetTcpLoad_Response>()
{
  return "xarm_msgs/srv/SetTcpLoad_Response";
}

template<>
struct has_fixed_size<xarm_msgs::srv::SetTcpLoad_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<xarm_msgs::srv::SetTcpLoad_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<xarm_msgs::srv::SetTcpLoad_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<xarm_msgs::srv::SetTcpLoad>()
{
  return "xarm_msgs::srv::SetTcpLoad";
}

template<>
inline const char * name<xarm_msgs::srv::SetTcpLoad>()
{
  return "xarm_msgs/srv/SetTcpLoad";
}

template<>
struct has_fixed_size<xarm_msgs::srv::SetTcpLoad>
  : std::integral_constant<
    bool,
    has_fixed_size<xarm_msgs::srv::SetTcpLoad_Request>::value &&
    has_fixed_size<xarm_msgs::srv::SetTcpLoad_Response>::value
  >
{
};

template<>
struct has_bounded_size<xarm_msgs::srv::SetTcpLoad>
  : std::integral_constant<
    bool,
    has_bounded_size<xarm_msgs::srv::SetTcpLoad_Request>::value &&
    has_bounded_size<xarm_msgs::srv::SetTcpLoad_Response>::value
  >
{
};

template<>
struct is_service<xarm_msgs::srv::SetTcpLoad>
  : std::true_type
{
};

template<>
struct is_service_request<xarm_msgs::srv::SetTcpLoad_Request>
  : std::true_type
{
};

template<>
struct is_service_response<xarm_msgs::srv::SetTcpLoad_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // XARM_MSGS__SRV__DETAIL__SET_TCP_LOAD__TRAITS_HPP_
